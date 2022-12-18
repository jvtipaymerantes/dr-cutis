/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

/** 
npx tailwindcss -i ./static/css/style.css -o ./static/css/dist/output.css --watch 
*/