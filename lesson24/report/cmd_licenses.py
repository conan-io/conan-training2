import json

from conan.api.conan_api import ConanAPI
from conan.api.output import ConanOutput, cli_out_write
from conan.cli.command import conan_command

def output_json(msg):
    cli_out_write(json.dumps(msg, indent=4))

def output_default(msg):
    cli_out_write(msg.get("greet", "No message provided"))

@conan_command(group="Reporting", formatters={"json": output_json, 
                                                     "text": output_default})
def licenses(conan_api: ConanAPI, parser, *args):
    """
    Simple command to print a message in stdout
    """
    parser.add_argument('message',
                        help="Message to print to stdout")
    args = parser.parse_args(*args)

    return {"greet":  args.message}
