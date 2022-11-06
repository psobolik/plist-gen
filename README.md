# plist-gen

Use this script to generate a macOS launchd service _plist_ from a _yaml_ file.

You can use _sample/launchd.example.plist_ as a template. It contains all of the fields
you might want to include in a service definition, with only the two required fields defined.
At a minimum, you will want to change those values.

The script writes its output to stdout, which you can redirect to a file.