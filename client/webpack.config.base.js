const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { resolve } = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

const filesToOutput = [
  { from: 'node_modules/bootstrap/dist/css/bootstrap.min.css', to: 'css/' },
  { from: 'node_modules/bootstrap/dist/css/bootstrap.min.css.map', to: 'css/' },
  { from: 'font/**', to: ''}
];

module.exports = {
  entry: './src/web-app.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, '..', 'www')
  },
  plugins: [
    new HtmlWebpackPlugin({inject: false, template: 'index.html'}),
    new CopyWebpackPlugin([ ...filesToOutput ], { ignore: [ '.DS_Store' ] })
  ],
  resolve: {
    extensions: [".js"],
    alias: {
      ["~"]: resolve(__dirname, "src")
    }
  }
};