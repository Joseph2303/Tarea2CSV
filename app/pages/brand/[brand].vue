<script setup lang="ts">
// @ts-nocheck
import { computed } from 'vue'
const brand = useRoute().params.brand as string

const { data: laptops } = await useAsyncData(`brand-${brand}`, () =>
  queryContent('/laptops').where({ brand }).find()
)
</script>

<template>
  <section class="brand-page">
    <h1>Marca: {{ decodeURIComponent($route.params.brand as string) }}</h1>
    <ul class="laptop-grid">
      <li v-for="lap in laptops" :key="lap._path" class="laptop-card">
        <NuxtLink :to="lap._path">
          <h2>{{ lap.brand }} {{ lap.model }}</h2>
          <p><strong>Procesador:</strong> {{ lap.processor }}</p>
          <p><strong>RAM:</strong> {{ lap.ram_gb }} GB</p>
          <p class="price">USD ${{ lap.price_usd }}</p>
        </NuxtLink>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.brand-page {
  padding: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}

.brand-page h1 {
  text-align: center;
  font-size: 2rem;
  color: #0077b6;
  margin-bottom: 2rem;
}

.laptop-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.5rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.laptop-card {
  background: #f8faff;
  padding: 1.2rem;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.laptop-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.12);
}

.laptop-card h2 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
  color: #03045e;
}

.laptop-card p {
  margin: 0.3rem 0;
  font-size: 0.95rem;
  color: #333;
}

.laptop-card .price {
  margin-top: 0.8rem;
  font-size: 1.1rem;
  font-weight: bold;
  color: #0077b6;
}

.laptop-card a {
  text-decoration: none;
  color: inherit;
  display: block;
}
</style>
