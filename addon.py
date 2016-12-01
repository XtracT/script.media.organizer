import xbmc
import xbmcaddon
import xbmcgui
import os
import shutil
import time
import resources.lib.untangle as untangle

###
#Checks if the file is a video or related file (nfo or srt have same name)
###
def find_file_type(filename):
	video_file_extensions = (
		'.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf', '.aec',
		'.aep', '.aepx', '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut', '.arf', '.asf',
		'.asx', '.avb', '.avc', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik',
		'.bin', '.bix', '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine',
		'.cip', '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dat',
		'.dav', '.dce', '.dck', '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm','.dmsm3d', '.dmss',
		'.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms','.dvx', '.dxr',
		'.dzm', '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp','.fcproject',
		'.ffd', '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp','.h264', '.hdmov',
		'.hkm', '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism', '.ismc', '.ismv', '.iva', '.ivf','.ivr', '.ivs',
		'.izz', '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg','.m1v', '.m21',
		'.m21', '.m2a', '.m2p', '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv','.mj2', '.mjp',
		'.mjpg', '.mk3d', '.mkv', '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie','.mp21',
		'.mp21', '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex','.mpl',
		'.mpl', '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb','.mvc',
		'.mvd', '.mve', '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv','.nvc', '.ogm',
		'.ogv', '.ogx', '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist','.plproj',
		'.pmf', '.pmv', '.pns', '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr','.pxv',
		'.qt', '.qtch', '.qtindex', '.qtl', '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm', '.rmd','.rmd',
		'.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp', '.rsx', '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk','.sbt',
		'.scc', '.scm', '.scm', '.scn', '.screenflow', '.sec', '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi','.smi',
		'.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.srt', '.ssf', '.ssm', '.stl', '.str', '.stx', '.svi', '.swf','.swi',
		'.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0', '.tpd', '.tpr', '.trp', '.ts','.tsp', '.ttxt',
		'.tvs', '.usf', '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx', '.veg', '.vem', '.vep', '.vf','.vft',
		'.vfw', '.vfz', '.vgz', '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob', '.vp3', '.vp6', '.vp7','.vpj',
		'.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv', '.wmx','.wot', '.wp3',
		'.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog',
		'.yuv', '.zeg','.zm1', '.zm2', '.zm3', '.zmv')

	audio_file_extensions = (
		'.midi', '.aiff', '.wave', '.aiff', '.ac3', '.dts', '.alac', '.amr', '.flac,', '.ape', '.ym', '.adpcm', '.cdda','.m4a',
		'.m4b', '.wv', '.webm', '.realaudio', '.shn', '.wavpack,', '.mpc', '.shorten', '.speex', '.it', '.s3m', '.mod','.xm',
		'.nsf', '.spc', '.gym', '.sid', '.adlib', '.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.amr', '.ape', '.au','.awb',
		'.dct', '.dss', 'dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4p', '.mmf', '.mp3', '.mpc', '.msv', '.ogg', '.oga','.mogg',
		'.opus', '.ra', '.rm', '.raw', '.sln', '.tta', '.vox', '.wav', '.wma')

	if filename.endswith((video_file_extensions)):
		return "Video"
	elif filename.endswith((audio_file_extensions)):
		return "Audio"
	else:
		return "Unknown"

def is_not_sample_file(full_filename):
	keywords = ('Sample','sample','SAMPLE','Trailer','trailer','TRAILER')
	size_file = os.path.getsize(full_filename)
	not_a_sample = [False for match in keywords if match in full_filename]

	if (not_a_sample == []) or (size_file > 100 * 1024 * 1024):
		not_a_sample = True
	else:
		not_a_sample = False
	return not_a_sample

def move_to_folder(full_filename,folder,filename):
	# Create destination folder if it does not exist and move file
	if not os.path.exists(folder):
		os.makedirs(folder)
	shutil.move(full_filename, os.path.join(folder, filename))

def load_settings():
	global source_folder, check_folder, delete_files, update_libraries, show_notifications, movies_folder, shows_folder, anime_folder, music_folder
	source_folder = xbmc.translatePath(__settings__.getSetting("source_folder"))
	check_folder = xbmc.translatePath(__settings__.getSetting("check_folder"))
	delete_files = bool(__settings__.getSetting("remove_files"))
	update_libraries = bool(__settings__.getSetting("update_libraries"))
	show_notifications = bool(__settings__.getSetting("show_notifications"))
	try:
		movies_folder = xbmc.translatePath(__settings__.getSetting("movies_folder"))
	except:
		movies_folder = check_folder
	try:
		shows_folder = xbmc.translatePath(__settings__.getSetting("shows_folder"))
	except:
		shows_folder = check_folder
	try:
		anime_folder = xbmc.translatePath(__settings__.getSetting("anime_folder"))
	except:
		anime_folder = check_folder
	try:
		music_folder = xbmc.translatePath(__settings__.getSetting("music_folder"))
	except:
		music_folder = check_folder

def send_notification(text,time):
	if show_notifications:
		xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (__addonname__, text, time, __icon__))

#Stop script execution if kodi is playing a file
if xbmc.Player().isPlaying():
	sys.exit()

#Get addon data
addon       = xbmcaddon.Addon()
__addonname__   = addon.getAddonInfo('name')
__settings__   = xbmcaddon.Addon(addon.getAddonInfo('id'))
__icon__ = addon.getAddonInfo('icon')

#Here a try catch to get settings, if not open settings dialogue
settings_loaded = False
while not settings_loaded:
	try:
		load_settings()
		settings_loaded = True
	except:
		#TO-DO: pop up to say first settings must be configured, if no folder selected media goes to Unorganizable files folder
		__settings__.openSettings()  # this will open settings window
		load_settings()
#TO-DO
create_symlink = True
#check stupid folders in movies


#Prepare script
if show_notifications: xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,'Initializing Media Organizer...', 100, __icon__))
video_organized = False
audio_organized = False

if os.path.isdir(source_folder):
	# Get total number of files to process
	file_count = 0
	for root, dirs, files in os.walk(source_folder, topdown=False):
		for filename in files:
			file_count = file_count + 1
	#file_count = 1
	if file_count > 0:
		fileNum = 0
		for root, dirs, files in os.walk(source_folder, topdown=False):
			for filename in files:
				fileNum = fileNum + 1
				full_filename = os.path.join(root, filename)
				file_type = find_file_type(full_filename)
				#xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (__addonname__, 'File ' + str(fileNum) + '/' + str(file_count) + ' - ' + file_type, 1, __icon__))

				if  file_type=="Video":
					video_organized = True
					info = untangle.Untangle(filename, use_meta_info=False)  # Get info from the file
					if bool(info.id) & is_not_sample_file(full_filename): #
						if info.type_video == "MOVIE":
							destination_folder = os.path.join(movies_folder,info.proper_title + " (" + str(info.year) + ")" )
						elif info.type_video == "SHOW":
							destination_folder = os.path.join(shows_folder,info.proper_title, "Season "  + str(info.season).zfill(2))
						elif info.type_video == "ANIME":
							destination_folder = os.path.join(anime_folder, info.proper_title, "Season " + str(info.season).zfill(2))
						else:
							destination_folder = os.path.join(check_folder,info.proper_title + " (" + str(info.year) + ")" )
						move_to_folder(full_filename, destination_folder, filename)
					elif not is_not_sample_file(full_filename):
						os.remove(full_filename)
					else:
						if delete_files:
							os.remove(full_filename)
						else:
							move_to_folder(full_filename, check_folder, filename)
				elif file_type=="Audio":
					audio_organized = True
					fileFolder = root.replace(source_folder, '')
					destination_folder = os.path.join(music_folder, fileFolder)
					move_to_folder(full_filename, destination_folder, filename)
				else:
					if delete_files:
						os.remove(full_filename)
					else:
						move_to_folder(full_filename, check_folder, filename)

			# Remove empty directories
			if os.listdir(root) == [] :
				if root!=source_folder:
					os.rmdir(root)

#Update the video library
if update_libraries & video_organized:
	send_notification(file_count + ' iles organized! Updating video library', 500)
	xbmc.executebuiltin('UpdateLibrary(video)')
	time.sleep(0.1)
	xbmc.executebuiltin('CleanLibrary(video)')
elif update_libraries & audio_organized:
	send_notification(file_count + ' iles organized! Updating music library', 500)
	xbmc.executebuiltin('UpdateLibrary(music)')
	time.sleep(0.1)
	xbmc.executebuiltin('CleanLibrary(music)')
elif file_count == 0:
	send_notification('No files to organize!', 200)
else:
	send_notification(file_count + ' files organized!', 200)