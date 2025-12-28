import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import federation from "@originjs/vite-plugin-federation"

export default defineConfig({
  plugins: [
    react(),
    federation({
      name: "devicesMf",
      filename: "remoteEntry.js",
      exposes: {
        "./Dashboard": "./src/Dashboard.jsx"
      },
      shared: ["react", "react-dom"]
    })
  ]
})
