project('PythonApp',
  version: '0.1.0',
  meson_version: '>= 0.59.4',
)

configure_file(
  input: 'main.py',
  output: 'main-run',
  copy: true,
  install: true,
  install_dir: get_option('bindir')
)
