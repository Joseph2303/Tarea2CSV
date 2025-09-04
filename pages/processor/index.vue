<script setup lang="ts">
// @ts-nocheck
import { computed } from 'vue'

const { data: docs } = await useAsyncData('all-proc', () =>
  queryContent('/laptops').only(['processor']).find()
)

const procs = computed(() =>
  Array.from(new Set((docs.value || []).map(d => d.processor))).sort()
)
</script>

<template>
  <section class="proc-list">
    <h1>Procesadores</h1>
    <ul>
      <li v-for="p in procs" :key="p">
        <NuxtLink :to="`/processor/${encodeURIComponent(p)}`">{{ p }}</NuxtLink>
      </li>
    </ul>
  </section>
</template>

<style scoped>
.proc-list {
  padding: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.proc-list h1 {
  text-align: center;
  font-size: 2rem;
  color: #0077b6;
  margin-bottom: 1.5rem;
}

.proc-list ul {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1rem;
  list-style: none;
  padding: 0;
  margin: 0;
}

.proc-list li {
  background: #f1f9fc;
  padding: 0.8rem 1rem;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.2s ease, background 0.3s ease;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.proc-list li:hover {
  background: #caf0f8;
  transform: translateY(-4px);
}

.proc-list a {
  text-decoration: none;
  color: #03045e;
  font-weight: 600;
  font-size: 1.05rem;
}
</style>
