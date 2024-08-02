/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Comfortaa', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
  daisyui: {
    themes: [{
      "mytheme": {
        "primary": "#af8f6f",
        "primary-content": "#292524",
        "secondary": "#74512d",
        "secondary-content": "#e2dad2",
        "accent": "#543310",
        "accent-content": "#dbd3cc",
        "neutral": "#f8f4e1",
        "neutral-content": "#292524",
        "base-100": "#f8f4e1",
        "base-200": "#d2bfad",
        "base-300": "#a4805b",
        "base-content": "#292524",
        "info": "#fef08a",
        "info-content": "#161407",
        "success": "#bef264",
        "success-content": "#0d1403",
        "warning": "#fbbf24",
        "warning-content": "#150d00",
        "error": "#ff0000",
        "error-content": "#160000",
      }
    }], // false: only light + dark | true: all themes | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: "dark", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: ":root", // The element that receives theme color CSS variables
  },
}
