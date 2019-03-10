# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

module purge
module load pgi
module load cuda
module load gnutools
