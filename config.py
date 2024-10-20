from configparser import ConfigParser


def get_config(filename="database2.ini", section="postgresql"):
  """
  Reads configuration details from a specified INI file and section.

  Args:
      filename (str, optional): Path to the configuration file. Defaults to "database.ini".
      section (str, optional): Name of the section containing database settings. Defaults to "postgresql".

  Returns:
      dict: A dictionary containing the parsed configuration values from the specified section.
          Returns an empty dictionary if the section is not found.

  Raises:
      IOError: If there's an error reading the configuration file.
  """

  parser = ConfigParser()
  try:
    parser.read(filename)
  except FileNotFoundError:
    raise IOError(f"Configuration file not found: {filename}")

  if not parser.has_section(section):
    return {}  # Return empty dictionary if section not found

  config = dict(parser.items(section))
  return config

# Example usage
config_dict = get_config()

# Access configuration values (fix typo)
host = config_dict.get("host")
dbname = config_dict.get("dbname")
username = config_dict.get("username")
password = config_dict.get("password")
port = config_dict.get("port")
