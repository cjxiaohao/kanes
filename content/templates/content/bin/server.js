var express   = require('express');
var path      = require('path');
var app       = express();
var snippet   = require ( 'grunt-contrib-livereload/lib/utils' ).livereloadSnippet;
var jinjs     = require ( 'jinjs' );
var fs        = require ( "fs" );
// jinjs.registerExtension ( ".html", function ( txt )
// {
//     console.log ( "111111111111111111111111111111111" );
// } );

app.set('port', process.env.PORT || 3000);
app.set('views', __dirname);
app.set('view engine', 'jinjs');
// app.register ( '.html', jinjs );
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(express.cookieParser('change this value to something unique'));
app.use(express.cookieSession());
app.use(express.compress());
app.use (
    function ( req, res, next ) {
        console.log ( "snippet middleware" );
        snippet ( req, res, next );
    }
 );

// app.set("view options", { jinjs_pre_compile: function (str) { return parse_pwilang(str); }, layout: false });
app.get ( '/view.html', function ( request, response )
{
    fs.readFile ( "view.jinjs", function ( error, data )
    {
        if ( error ) throw error;
        opts = {
            jinjs_pre_compile: function ( str ) {},
            filename: 'view.jinjs',
            root: path.dirname ( 'view.jinjs' ),
            app: app,
        };

        console.log ( "indexOf" );
        console.log ( data.toString ( ) );

        response.send ( jinjs.compile ( data.toString ( ), opts ) );
    } );
} );
app.use ( express.static(path.join(__dirname, '../')));
app.use(app.router);

if ('development' === app.get('env')) {
  app.use(express.errorHandler());
}

module.exports = app.listen(app.get('port'), function() {
  console.log("Express server listening on port " + app.get('port'));
});
