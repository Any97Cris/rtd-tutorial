API
===

.. autosummary::
   :toctree: generated

.. raw:: html

    <div>Teste</div>

    <div id="swagger-ui"></div>

    <script src="_static/swagger-ui/swagger-ui-bundle.js"></script>
    <script src="_static/swagger-ui/swagger-ui-standalone-preset.js"></script>
    <script>
      const ui = SwaggerUIBundle({
        url: "https://libresign.github.io/api/",  // Caminho para o seu arquivo OpenAPI JSON
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIStandalonePreset
        ],
        layout: "StandaloneLayout"
      });
    </script>