<template>
  <div className="pdf-upload">
    <input type="file" @change="onFileChange" accept=".pdf"/>
    <div v-if="fileName" className="file-name">{{ fileName }}</div>
  </div>
</template>

<script>
export default {
  name: 'PdfUpload',
  data() {
    return {
      fileName: null,
    };
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file && file.type === 'application/pdf') {
        console.log('Emitting file-uploaded event with file:', file);
        this.$emit('file-uploaded', file);
        this.fileName = file.name;
      } else {
        alert('Please upload a PDF file.');
      }
    },
  },
};
</script>

<style scoped>
.pdf-upload {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.file-name {
  font-size: 1rem;
  font-weight: bold;
  color: #007bff;
  margin-top: 0.5rem;
}
</style>
