// nuxt.config.ts
export default defineNuxtConfig({
  srcDir: 'app/',                       // <<— clave para usar /app como raíz
  modules: ['@nuxt/content'],
  components: [{ path: '~/components', pathPrefix: false }],
  app: { head: { title: 'Catálogo de Laptops' } }
})
