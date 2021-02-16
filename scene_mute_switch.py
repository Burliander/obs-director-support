import obspython as obs

audio_sources = []

#names of audio sources which shall not be muted on switch to specif scene
ignore_unmute_sources = ["NAME_OF_AUDIO_SOURCE1","NAME_OF_AUDIO_SOURCE2"]
#specific scene were audio sources shall be muted
mute_on_scenename = "alle"

def set_audio_sources():

	sources = obs.obs_enum_sources()

	for source in sources:

		if obs.obs_source_get_type(source) == obs.OBS_SOURCE_TYPE_INPUT:
			capabilities = obs.obs_source_get_output_flags(source)
			has_audio = capabilities & obs.OBS_SOURCE_AUDIO
			if has_audio:
				audio_sources.append(source)

	obs.source_list_release(sources)

def mute(ismute):
	for audio_source in audio_sources:
		print(obs.obs_source_get_name(audio_source))
		if not (obs.obs_source_get_name(audio_source) in ignore_unmute_sources):		
			obs.obs_source_set_muted(audio_source, ismute)
			

def on_event(event):
	if event == obs.OBS_FRONTEND_EVENT_SCENE_CHANGED:
		mute((mute_on_scenename == (obs.obs_source_get_name(obs.obs_frontend_get_current_scene()))))


def script_load(settings):
	print("OBS mute scene switch script loaded.")
	set_audio_sources()
	obs.obs_frontend_add_event_callback(on_event)


def script_unload():
	print("OBS mute scene switch script unloaded.")
