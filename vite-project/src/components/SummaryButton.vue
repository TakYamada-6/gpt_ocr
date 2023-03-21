<template>
  <div>
    <button class="upload-button" @click="sendFileToAPI">要約</button>
    <div v-if="responseReceived" class="response-container">
      <h2>API Response:</h2>
      <pre class="response-content">{{ response }}</pre>
    </div>
    <div v-if="isLoading" class="loading-overlay">
      <div class="loader"></div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'SummaryButton',
  props: {
    buttonText: {
      type: String,
      default: 'Summary'
    },
    uploadedFile: {
      type: File,
      required: true
    }
  },
  setup(props) {
    const response = ref(null);
    const responseReceived = ref(false);
    const isLoading = ref(false);

    const sendFileToAPI = async () => {
      if (!props.uploadedFile) {
        alert('Please upload a file first.');
        return;
      }

      const formData = new FormData();
      formData.append('file', props.uploadedFile);

      try {
        isLoading.value = true;
        const responseRaw = await fetch('http://localhost:8000/api/summarize_resume', {
          method: 'POST',
          body: formData
        });
        const responseData = await responseRaw.json();
        response.value = responseData;
        responseReceived.value = true;
      } catch (error) {
        console.error('Error while sending the file:', error);
        alert('An error occurred while sending the file. Please try again.');
      } finally {
        isLoading.value = false;
      }
    };

    return {
      response,
      responseReceived,
      sendFileToAPI,
      isLoading,
    };
  }
};
</script>

<style scoped>

.response-content {
  font-family: "Courier New", Courier, monospace;
  color: #2c3e50;
}
</style>
