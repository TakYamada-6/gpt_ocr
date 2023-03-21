import { defineConfig } from 'npm:vite@^4.0.4'
import vue from 'npm:@vitejs/plugin-vue@^4.0.0'

import 'npm:vue@^3.2.45'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
   server: {
    proxy: {
        '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        ws: true,
        },
         '/ws': {
        target: 'ws://127.0.0.1:8000',
        ws: true,
        changeOrigin: true,
      },
    },
  },
})
