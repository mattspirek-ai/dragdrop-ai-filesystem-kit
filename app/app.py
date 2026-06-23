from flask import Flask, request, jsonify, send_from_directory, render_template_string
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename
from PIL import Image
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ORGANIZED_FOLDER = 'organized'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'docx', 'txt', 'xlsx'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ORGANIZED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

HTML_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>DragDrop AI File System</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .dropzone { transition: all 0.2s; }
        .dropzone.dragover { background: #22d3ee; color: black; transform: scale(1.03); }
        .file-card { animation: pop 0.3s; }
        @keyframes pop { 0% {transform: scale(0.8); opacity:0} 100% {transform:scale(1); opacity:1} }
    </style>
</head>
<body class="bg-zinc-950 text-zinc-100">
    <div class="max-w-6xl mx-auto p-8">
        <div class="flex justify-between items-center mb-10">
            <div class="flex items-center gap-4">
                <div class="w-12 h-12 bg-cyan-500 rounded-3xl flex items-center justify-center text-3xl">📦</div>
                <div>
                    <h1 class="text-5xl font-bold tracking-tighter">DragDrop AI</h1>
                    <p class="text-cyan-400 text-xl">Intelligent File System</p>
                </div>
            </div>
            <div class="text-sm font-mono bg-zinc-900 px-6 py-3 rounded-3xl border border-cyan-900">Standalone • Self-hosted • Local-first</div>
        </div>
        
        <div class="grid grid-cols-12 gap-8">
            <!-- Drop Zone -->
            <div class="col-span-7">
                <div id="dropzone" 
                     class="dropzone border-4 border-dashed border-cyan-500 hover:border-white h-[420px] rounded-3xl flex flex-col items-center justify-center text-center cursor-pointer bg-zinc-900">
                    <div class="text-7xl mb-6">⬇️</div>
                    <h2 class="text-3xl font-semibold mb-3">Drop files here</h2>
                    <p class="max-w-xs text-zinc-400">AI will auto-categorize, extract insights, tag, and organize them into smart folders.</p>
                    <input type="file" id="fileInput" multiple class="hidden">
                    <div class="mt-10 text-xs px-8 py-3 border border-dashed border-zinc-700 rounded-2xl">or click to select files</div>
                </div>
            </div>
            
            <!-- Library -->
            <div class="col-span-5">
                <div class="bg-zinc-900 border border-zinc-700 rounded-3xl p-6 h-full">
                    <div class="flex items-center justify-between mb-6">
                        <h3 class="font-semibold text-lg">Organized Library</h3>
                        <span id="count" class="text-xs bg-zinc-800 px-4 py-1 rounded-3xl">0 files</span>
                    </div>
                    <div id="library" class="space-y-3 max-h-[340px] overflow-auto text-sm"></div>
                </div>
            </div>
        </div>
        
        <div class="mt-12 text-xs text-zinc-500 flex items-center gap-8 border-t border-zinc-800 pt-8">
            <div>Built as standalone offer kit. Fully local. No cloud. AI simulation uses local rules + metadata extraction.</div>
            <button onclick="window.location.reload()" 
                    class="bg-white text-black px-6 py-2.5 rounded-2xl text-xs font-medium">Reset Demo</button>
        </div>
    </div>

    <script>
        let fileCount = 0;
        const dropzone = document.getElementById('dropzone');
        const library = document.getElementById('library');
        const countEl = document.getElementById('count');
        const fileInput = document.getElementById('fileInput');

        function simulateAIProcessing(filename, ext) {
            const categories = ['Reports', 'Images', 'Data', 'Contracts', 'Research'];
            const category = categories[Math.floor(Math.random()*categories.length)];
            const tags = ['ai-processed', 'auto-tagged', ext];
            const summary = `AI Summary: Document processed on ${new Date().toLocaleDateString()}. Key topics detected.`;
            
            const card = document.createElement('div');
            card.className = 'file-card bg-zinc-950 border border-zinc-700 p-4 rounded-2xl flex gap-4';
            card.innerHTML = `
                <div class="text-4xl flex-shrink-0">${ext === 'pdf' ? '📕' : ext.includes('img') ? '🖼️' : '📄'}</div>
                <div class="flex-1 min-w-0">
                    <div class="font-medium truncate">${filename}</div>
                    <div class="text-[10px] text-emerald-400">→ ${category}/</div>
                    <div class="text-xs text-zinc-500 mt-2 line-clamp-2">${summary}</div>
                    <div class="flex gap-2 mt-3">
                        ${tags.map(t => `<span class="text-[9px] px-3 py-0.5 bg-zinc-900 rounded-full">${t}</span>`).join('')}
                    </div>
                </div>
            `;
            library.prepend(card);
            fileCount++;
            countEl.textContent = `${fileCount} files`;
        }

        dropzone.addEventListener('click', () => fileInput.click());
        fileInput.addEventListener('change', e => handleFiles(e.target.files));

        dropzone.addEventListener('dragover', e => {
            e.preventDefault();
            dropzone.classList.add('dragover');
        });
        dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
        dropzone.addEventListener('drop', e => {
            e.preventDefault();
            dropzone.classList.remove('dragover');
            handleFiles(e.dataTransfer.files);
        });

        function handleFiles(files) {
            Array.from(files).forEach(file => {
                if (file.size > 50*1024*1024) return; // limit
                const ext = file.name.split('.').pop().toLowerCase();
                simulateAIProcessing(file.name, ext);
                
                // In real version this would POST to /upload
                console.log(`Processed: ${file.name}`);
            });
        }

        // Seed demo files
        setTimeout(() => {
            simulateAIProcessing("Q3_Financial_Summary.pdf", "pdf");
            setTimeout(() => simulateAIProcessing("team_photo_field_visit.jpg", "jpg"), 450);
            setTimeout(() => simulateAIProcessing("project_requirements_v2.docx", "docx"), 1100);
        }, 600);
    </script>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file'}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    # Simulate AI organization
    category = "Reports" if 'report' in filename.lower() else "Documents"
    organized_path = os.path.join(ORGANIZED_FOLDER, category, filename)
    os.makedirs(os.path.dirname(organized_path), exist_ok=True)
    shutil.copy(filepath, organized_path)
    
    metadata = {
        "filename": filename,
        "processed_at": datetime.now().isoformat(),
        "category": category,
        "tags": ["ai-processed", "auto-categorized"],
        "size_kb": round(os.path.getsize(organized_path)/1024, 1)
    }
    
    with open(organized_path + '.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return jsonify({'status': 'success', 'category': category, 'metadata': metadata})

@app.route('/files')
def list_files():
    files = []
    for root, _, filenames in os.walk(ORGANIZED_FOLDER):
        for fname in filenames:
            if not fname.endswith('.json'):
                files.append({
                    'name': fname,
                    'path': os.path.relpath(os.path.join(root, fname), ORGANIZED_FOLDER)
                })
    return jsonify(files)

if __name__ == '__main__':
    print("🚀 Starting DragDrop AI File System - http://127.0.0.1:8080")
    app.run(host='0.0.0.0', port=8080, debug=False)
