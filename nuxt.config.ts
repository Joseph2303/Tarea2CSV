export default defineNuxtConfig({
  srcDir: 'app/',
  modules: ['@nuxt/content'],
  components: [{ path: '~/components', pathPrefix: false }],
  nitro: {
    prerender: {
      failOnError: false   // no detiene el build por 404
      // routes: []        // o define rutas extra si las necesitas
    }
  }
})
