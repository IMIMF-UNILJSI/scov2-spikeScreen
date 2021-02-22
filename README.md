# scov2-spikeScreen
SCOV2-spikeScreen IMI prototype bash pipeline

## build container

/path/to/repo/directory/buildContainer web # pull from shub

or

/path/to/repo/directory/buildContainer # build from scratch

## Running

Create a working dir somewhere in your FS (preferably outside of the git dir), run:

singularity run --bind /path/to/repo/directory:/opt,/path/to/data:/mnt /path/to/repo/directory/spikeScreenContainer.sif /opt/runPipeline runID /mnt

## Cleanup

A cleanup script is also provided (see repo directory: cleanUp), but it may not be so useful. It simply removes the contents of the work dir related to the pipeline process.

