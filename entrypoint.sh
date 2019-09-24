#!/usr/bin/env sh

if test -z "$WILLAMETTE_APP"; then
    echo "WILLAMETTE_APP environment variable must be set."
    exit 1
fi
case $WILLAMETTE_APP in
    api)
        echo "Creating/Upgrading database"
        flask db init
        echo "Running the API app"
        exec gunicorn -c "python:willamette.config.gunicorn_config" "willamette.app:create_app()"
        ;;
     *)
        echo "Invalid app: $WILLAMETTE_APP"
        exit 2
esac
