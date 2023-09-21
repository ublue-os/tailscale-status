%global uuid tailscale-status@maxgallup.github.com

Name:        gnome-shell-extension-tailscale-status
Version:     {{{ git_dir_version }}}
Release:     1%{?dist}
Summary:     An unofficial Gnome Extension to manage and check the status of tailscale-cli.

Group:       User Interface/Desktops
License:     GPLv2
URL:         https://github.com/ublue-os/gnome-shell-extension-tailscale-status
Source0:     %{url}/archive/refs/heads/main.tar.gz
BuildArch:   noarch

Requires:    gnome-shell >= 3.12
%description
An unofficial Gnome Extension to manage and check the status of tailscale-cli. This extension is in no way affiliated with Tailscale Inc.

%prep
%autosetup -n gnome-shell-extension-tailscale-status-main

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r %{uuid}/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}