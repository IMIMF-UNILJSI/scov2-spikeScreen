# scov2-spikeScreen
SCOV2-spikeScreen IMI prototype bash pipeline

## build container

/path/to/repo/directory/buildContainer web # pull from shub

or

/path/to/repo/directory/buildContainer local # build from scratch

no argument defaults to "web", local requires sudo privileges. If none of the options is suitable to the user, do manual build with working parameter settings. 

## Running

Create a working dir somewhere in your FS (preferably outside of the git dir), run:

singularity run --bind /path/to/repo/directory:/opt/scripts,/path/to/data:/mnt /path/to/repo/directory/spikeScreenContainer.sif /opt/runPipeline runID keyword /mnt

The second argument (keyword) should be replaced with either pools/assemblies/nib to run the appropriate analysis (self explanatory).

## Cleanup

A cleanup script is also provided (see repo directory: cleanUp), but it may not be so useful. It simply removes the contents of the work dir related to the pipeline process.

