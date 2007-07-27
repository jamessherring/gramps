#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2007  Donald N. Allingham
# Copyright (C) 2007       Brian G. Matherly
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

from Simple import SimpleAccess, by_date, SimpleDoc
from gettext import gettext as _

def run(database, document, person):
    
    sa = SimpleAccess(database)
    sd = SimpleDoc(document)

    # get the personal events
    event_list = sa.events(person)

    # get the events of each family in which the person is 
    # a parent
    for family in sa.parent_in(person):
        event_list += sa.events(family)

    # Sort the events by their date
    event_list.sort(by_date)

    # display the results

    sd.title(_("Sorted events of %s") % sa.name(person))
    sd.paragraph("")

    sd.header1("\t".join(_("Event Type"),_("Event Date"),_("tEvent Place")))

    for event in event_list:
        sd.paragraph("%-12s\t%-12s\t%s" % (sa.event_type(event), 
                                           sa.event_date(event), 
                                           sa.event_place(event)))
