pkg_origin=kellpossible
pkg_name=swe30004
pkg_version=0.2.0
pkg_maintainer="Luke Frisken <l.frisken@gmail.com>"
pkg_license=()
pkg_upstream_url=https://github.com/habitat-sh/habitat-example-plans
pkg_source=nosuchfile.tar.gz
pkg_deps=(
	core/python/3.5.2/20160926155828
	core/postgresql/9.5.3/20160926180143
	core/glibc
)
pkg_build_deps=(core/gcc)
pkg_expose=(8090)


do_download() {
  return 0
}

do_verify() {
  return 0
}

do_unpack() {
  return 0
}


do_build() {
	# The mytutorialapp source code is in a relative directory, so you must copy the
  	# contents of the source directory into your $HAB_CACHE_SRC_PATH/$pkg_dirname as this
  	# is the same path that Habitat would use if you downloaded a tarball of the source code.
	cp -vr $PLAN_CONTEXT/../* $HAB_CACHE_SRC_PATH/$pkg_dirname
}

do_install() {
	# Our source files were copied over to HAB_CACHE_SRC_PATH/$pkg_dirname in do_build(),
	# and now they need to be copied from that directory into the root directory of our package
	# through the use of the pkg_prefix variable.
	cp main.py ${pkg_prefix}
	cp manage.py ${pkg_prefix}
	cp config.py ${pkg_prefix}

	cp -vr migrations/ ${pkg_prefix}
	cp -vr app/ ${pkg_prefix}

	# installs python packages required
	pip install -r $PLAN_CONTEXT/../requirements.txt
}