import json
import os

def create_available_list():
    attractors_dir = "attractors"
    output_file = "available_list.md"

    if not os.path.exists(attractors_dir):
        print(f"Error: Directory '{attractors_dir}' not found.")
        return

    available_attractors = []
    for filename in os.listdir(attractors_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(attractors_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data.get("available") and data.get("contact_ok"):
                        available_attractors.append(data)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error reading or parsing {filepath}: {e}")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("## 今週稼働可能アトラクター一覧\n\n")
        if not available_attractors:
            f.write("現在稼働可能なアトラクターはいません。\n")
        else:
            for attractor in available_attractors:
                name = attractor.get("name", "N/A")
                skills = ", ".join(attractor.get("skills", []))
                available_time = attractor.get("available_time", "N/A")
                note = attractor.get("note", "N/A")

                f.write(f"- {name}（{skills}）\n")
                f.write(f"  - 稼働可能時間：{available_time}\n")
                f.write(f"  - 備考：{note}\n\n")

    print(f"Successfully created {output_file}")

if __name__ == "__main__":
    create_available_list()
