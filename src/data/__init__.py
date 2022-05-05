from AirSim import AirSimData


data_sources = {"airsim": AirSimData}

def get_data_source(name):
	return data_sources[name.lower()]
