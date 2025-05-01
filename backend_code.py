import warnings
import scratchattach as sa
warnings.filterwarnings('ignore', category=sa.LoginDataWarning)
session = sa.login("sc-jcat", "jason@scratch")
server = sa.init_cloud_server()
