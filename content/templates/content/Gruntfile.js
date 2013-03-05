var snippet = require ( 'grunt-contrib-livereload/lib/utils' ).livereloadSnippet;
// middleware return [ require ( 'grunt-contrib-livereload/lib/utils' ).livereloadSnippet ]
// 必须出错，但是如果在之前用var就没有问题

module.exports = function ( grunt ) {
    grunt.initConfig ( {
        copy: {
            css: {
                files: [
                    { src: [ 'bootstrap.css', 'bootstrap-responsive.css' ], dest: 'public/css/',
                      cwd: 'components/bootstrap/docs/assets/css/', expand: true },
                    { src: [ 'main.css' ], dest: 'public/css/' },
                ]
            },
            img: {
                files: [
                    { src: [ '*' ], dest: 'public/img/', cwd: 'components/bootstrap/img/', expand: true }
                ]
            },
            js: {
                files: [
                    { src: [ 'bootstrap.js' ], dest: 'public/js/', cwd: 'components/bootstrap/docs/assets/js/', expand: true },
                    { src: [ 'jquery.js' ], dest: 'public/js/', cwd: 'components/jquery/', expand: true }
                ]
            }
        },

        regarde: {
            css: {
                files: '*.css',
                tasks: [ 'copy' ]
            }
        },

        server: {
            script: "bin/server.js"
        },

        connect: {
            liverealod: {
                // files: [ "." ],
                options: {
                    // base: __dirname,
                    middleware: function ( connect, options ) {
                        return [ snippet,
                                 connect.static ( require ( "path" ).resolve ( "." ) ) ];
                    }
                }
            }
        }
    } );

    grunt.loadNpmTasks ( "grunt-contrib" );
    grunt.loadNpmTasks ( "grunt-regarde" );
    grunt.loadNpmTasks ( "grunt-contrib-livereload" );
    grunt.loadNpmTasks ( "grunt-express-server" );

    grunt.registerTask ( 'default', [ ] );
    grunt.registerTask ( 'server',  [ 'livereload-start', 'express-server', 'regarde' ] );
};