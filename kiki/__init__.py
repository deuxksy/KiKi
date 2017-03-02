#-*- coding: utf-8 -*-
import os

from cryptography.fernet import Fernet

crypto = Fernet(os.getenv('ZZIZILY_KIKI_CRYPTO'))
package_name = 'kiki'
project_home = os.getenv('ZZIZILY_KIKI_HOME')