<script setup lang="ts">
// @ts-nocheck
import { computed } from 'vue'

const { data: docs } = await useAsyncData('all-brands', () =>
  queryContent('/laptops').only(['brand']).find()
)

const brands = computed(() =>
  Array.from(new Set((docs.value || []).map(d => d.brand))).sort()
)
</script>

<template>
  <section class="brands">
    <h1>Marcas</h1>
    <ul>
      <li v-for="b in brands" :key="b">
        <NuxtLink :to="`/brand/${encodeURIComponent(b)}`">{{ b }}</NuxtLink>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.brands {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.brands h1 {
  text-align: center;
  font-size: 2rem;
  color: #0077b6;
  margin-bottom: 1.5rem;
}

.brands ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.brands li {
  background: #f1f9fc;
  padding: 0.8rem 1rem;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.2s ease, background 0.3s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.brands li:hover {
  background: #caf0f8;
  transform: translateY(-4px);
}

.brands a {
  text-decoration: none;
  color: #03045e;
  font-weight: 600;
  font-size: 1.05rem;
}
</style>