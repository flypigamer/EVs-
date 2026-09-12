name: Build Android APK
on: [push, workflow_dispatch]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build with Buildozer
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential git python3-pip
          pip3 install buildozer
          buildozer android debug
      - name: Upload APK
        uses: actions/upload-artifact@v2
        with:
          name: discord-gen-apk
          path: bin/*.apk
