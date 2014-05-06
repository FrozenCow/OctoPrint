from flask import request, jsonify, make_response, url_for, send_from_directory

import os
import octoprint.gcodefiles as gcodefiles
import octoprint.util as util
from octoprint.filemanager.destinations import FileDestinations
from octoprint.settings import settings, valid_boolean_trues
from octoprint.server import printer, gcodeManager, eventManager, restricted_access, SUCCESS
from octoprint.server.util import redirectToTornado
from octoprint.server.ajax import ajax

@ajax.route("/stlfiles/<string:filename>.stl", methods=["GET"])
@restricted_access
def getSTLFile(filename):
  file = filename + ".stl"
  return send_from_directory(gcodeManager._uploadFolder,file)