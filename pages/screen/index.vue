<script setup lang="ts">
// @ts-nocheck
import { computed } from 'vue'

const { data: docs } = await useAsyncData('all-screens', () =>
  queryContent('/laptops').only(['screen_cm']).find()
)

const sizes = computed(() =>
  Array.from(new Set((docs.value || []).map(d => d.screen_cm))).sort((a: number, b: number) => a - b)
)
</script>

<template>
  <section class="screen-list">
    <h1>Tamaño de Pantalla (cm)</h1>
    <ul>
      <li v-for="s in sizes" :key="s">
        <NuxtLink :to="`/screen/${encodeURIComponent(String(s))}`">{{ s }} cm</NuxtLink>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.screen-list {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.screen-list h1 {
  text-align: center;
  font-size: 2rem;
  color: #0077b6;
  margin-bottom: 1.5rem;
}

.screen-list ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.screen-list li {
  background: #f1f9fc;
  padding: 0.8rem 1rem;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.2s ease, background 0.3s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.screen-list li:hover {
  background: #caf0f8;
  transform: translateY(-4px);
}

.screen-list a {
  text-decoration: none;
  color: #03045e;
  font-weight: 600;
  font-size: 1rem;
}
</style>
