import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',          // allow external access from Docker
    port: 5173,               // internal container port
    strictPort: true,         // fail if port is taken (good for Docker clarity)
    proxy: {
      '/api': 'http://localhost:8000', // proxy API calls to FastAPI backend
    }
  }
})
