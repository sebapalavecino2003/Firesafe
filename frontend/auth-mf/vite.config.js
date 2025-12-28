import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import federation from "@originjs/vite-plugin-federation"

export default defineConfig({
  plugins: [
    react(),
    federation({
      name: "authMf",
      filename: "remoteEntry.js",
      exposes: {
        "./Login": "./src/Login.jsx"
      },
      shared: ["react", "react-dom"]
    })
  ]
})
