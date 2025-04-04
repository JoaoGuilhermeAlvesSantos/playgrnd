BASE_DIR="$PWD"

if [ -z "$1" ]; then
    echo "$0 Missing <json(s) dir>"
    exit 1
fi

# Diretório base passado como argumento
TARGET_DIR="$1"

for file in "$TARGET_DIR"/*.json; do
    jq '.' "$file"
done