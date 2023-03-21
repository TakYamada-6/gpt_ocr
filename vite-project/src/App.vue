<template>
  <div id="app">
    <pdf-upload></pdf-upload>
  </div>
</template>

<script>
import PdfUpload from "./components/PdfUpload.vue";

export default {
  name: "App",
  components: {
    PdfUpload,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
