import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    strictPort: true, // fail loudly instead of drifting to 5174
    proxy: {
      // Forward /api/* to FastAPI. 127.0.0.1, not localhost, avoids an IPv6 mismatch.
      "/api": "http://127.0.0.1:8000",
    },
  },
});