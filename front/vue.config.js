const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "合肥市锦城小学社团资料收集平台";
      return args;
    });
  },
  transpileDependencies: true
})
