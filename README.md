# scov2-spikeScreen
SCOV2-spikeScreen IMI prototype bash pipeline

## build container

/path/to/repo/directory/buildContainer web # pull from shub

or

/path/to/repo/directory/buildContainer # build from scratch

## Running

Create a working dir somewhere in your FS (preferably outside of the git dir), run:

singularity run /path/to/repo/directory/spikeScreenContainer.sif /path/to/repo/directory/runPipeline <runID> </path/to/data_folder> 
