from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from django.conf import settings
from pathlib import Path
import os

@require_GET
def serve_service_worker(request):
    # prefer project root (BASE_DIR), fallback to current app dir
    root_path = Path(settings.BASE_DIR) / "service-worker.js"
    app_path = Path(__file__).resolve().parent / "service-worker.js"

    file_path = root_path if root_path.exists() else app_path
    if not file_path.exists():
        return HttpResponseNotFound("service-worker.js not found")

    with open(file_path, "rb") as f:
        return HttpResponse(f.read(), content_type="application/javascript")