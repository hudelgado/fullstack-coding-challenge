const merge = require('webpack-merge');
const baseConfig = require('./webpack.config.base.js');

module.exports = merge(baseConfig, {
  mode: 'development',
  devServer: {
    contentBase: './../www',
    historyApiFallback: true,
    host: '0.0.0.0'
  }
});