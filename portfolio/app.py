from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_project_data():
    projects = []
    projects_dir = os.path.join(app.static_folder, 'projects')
    
    for project_dir in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project_dir)
        if os.path.isdir(project_path):
            info_file = os.path.join(project_path, 'info.json')
            if os.path.exists(info_file):
                with open(info_file, 'r') as f:
                    project_info = json.load(f)
                    project_info['id'] = project_dir
                    project_info['image_folder'] = f'projects/{project_dir}'
                    projects.append(project_info)
    
    return projects

@app.route('/')
def index():
    projects = load_project_data()
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True, host= '192.168.1.7', port=5000)