#Updating the environment variables and sourcing the profile to apply changes
sudo env-update
# Adding the local service to the default runlevel to ensure it starts on boot
rc-update add local default