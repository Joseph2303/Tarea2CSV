<script setup lang="ts">
// @ts-nocheck
import { computed } from 'vue'

const { data: docs } = await useAsyncData('all-os', () =>
  queryContent('/laptops').only(['os']).find()
)

const oses = computed(() =>
  Array.from(new Set((docs.value || []).map(d => d.os))).sort()
)
</script>

<template>
  <section class="os-list">
    <h1>Sistema Operativo</h1>
    <ul>
      <li v-for="o in oses" :key="o">
        <NuxtLink :to="`/os/${encodeURIComponent(o)}`">{{ o }}</NuxtLink>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.os-list {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.os-list h1 {
  text-align: center;
  font-size: 2rem;
  color: #0077b6;
  margin-bottom: 1.5rem;
}

.os-list ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.os-list li {
  background: #f1f9fc;
  padding: 0.8rem 1rem;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.2s ease, background 0.3s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.os-list li:hover {
  background: #caf0f8;
  transform: translateY(-4px);
}

.os-list a {
  text-decoration: none;
  color: #03045e;
  font-weight: 600;
  font-size: 1.05rem;
}
</style>
