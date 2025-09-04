<template>
  <nav class="navbar">
    <NuxtLink to="/">Inicio</NuxtLink>
    <NuxtLink to="/brand">Por Marca</NuxtLink>
    <NuxtLink to="/os">Por Sistema Operativo</NuxtLink>
    <NuxtLink to="/screen">Por Tamaño de Pantalla</NuxtLink>
    <NuxtLink to="/processor">Por Procesador</NuxtLink>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  gap: 1.5rem;
  padding: 1rem 2rem;
  background: linear-gradient(90deg, #00b4d8, #90e0ef); /* celeste degradado */
  border-bottom: 2px solid #0077b6;
  justify-content: center;
  align-items: center;
}

.navbar a {
  text-decoration: none;
  color: #fff;
  font-weight: 600;
  transition: color 0.3s ease, transform 0.2s ease;
}

.navbar a:hover {
  color: #03045e;
  transform: scale(1.05);
}

.navbar a.router-link-active {
  border-bottom: 2px solid #03045e;
  padding-bottom: 2px;
}
</style>
