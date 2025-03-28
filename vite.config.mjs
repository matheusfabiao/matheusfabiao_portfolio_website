import { defineConfig } from 'vite';
import { resolve } from 'path';
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
    base: "/static/",
    build: {
      manifest: "manifest.json",
      outDir: resolve("./src/static/dist"),
      assetsDir: "assets",
      emptyOutDir: true,  // Limpa o diretório ao rebuildar
      rollupOptions: {
        input: {
          main: resolve("./src/static/js/main.js")
        }
      }
    },
    plugins: [
        tailwindcss()
    ]
  })