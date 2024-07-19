<template>
  <div class="docs-container">
    <iframe src="http://localhost:5001/docs" frameborder="0" class="docs-iframe"></iframe>
  </div>
</template>

<script>
export default {
  name: 'be_docs'
}
</script>

<style>
.docs-container {
  width: 100%;
  height: 100vh; /* Adjust height as needed */
}

.docs-iframe {
  width: 100%;
  height: 100%;
  border: none;
}
</style>
