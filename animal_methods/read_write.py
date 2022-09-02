from animal_methods.the_zoo import logger
from fast_API_base import app


@app.get("/leaflets/{leaflet_path:path}")
async def read_leaflet(leaflet_path: str):
    with open(leaflet_path, 'r') as leaflet:
        leaflet_contents = leaflet.read()
    return {"leaflet_contents": leaflet_contents}
# Run with 127.0.0.1:8000/leaflets/animal_methods/a_leaflet.txt
