{ pkgs, ... }: {
  channel = "stable-24.05";

  packages = [
    pkgs.python310
    pkgs.uv
  ];

  idx = {
    extensions = [ "ms-python.python" ];

    workspace = {
      onCreate = {
        install = ''
          uv venv .venv
          source .venv/bin/activate
          uv sync

          mkdir -p public
          cat > public/index.html << 'EOF'
          <!DOCTYPE html><html><body>
          <h2>LangGraph MCP Client</h2>
          <button onclick="call()">Call MCP Server</button>
          <pre id="out">Waiting...</pre>
          <script>
            async function call() {
              try {
                const res = await fetch("https://<replace-backend-url>/run", {
                  method: "POST",
                  headers: { "Content-Type": "application/json" },
                  body: JSON.stringify({ foo: "bar" })
                });
                const data = await res.json();
                document.getElementById("out").innerText = JSON.stringify(data, null, 2);
              } catch (e) {
                document.getElementById("out").innerText = "Error: " + e.message;
              }
            }
          </script>
          </body></html>
          EOF
        '';
        default.openFiles = [ "main.py" "public/index.html" ];
      };
    };

    previews = {
      enable = true;
      previews = {
        # 🔁 Backend (API)
        api = {
          command = [ "sh" "-c" "uv run uvicorn main:app --host 0.0.0.0 --port $PORT" ];
          manager = "web";
          env = { PORT = "$PORT"; };
        };

        # 🌐 Frontend (Static HTML)
        web = {
          command = [ "sh" "-c" "python3 -m http.server $PORT --directory public" ];
          manager = "web";
          env = { PORT = "$PORT"; };
        };
      };
    };
  };
}
