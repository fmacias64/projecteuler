package uk.co.mandg.thinkfoliotargetadapt;

import javax.persistence.EntityManagerFactory;

import uk.co.mandg.mgcommon.MgLogger;
import uk.co.mandg.thinkfoliotargetadapt.db.ThinkTransferDao;

/* MODULE      : ApplyStrategies.java
*
* NAME         : uk/co/mandg/thinkfoliotargetadapt/ApplyStrategies.java
*
* DESCRIPTION  : Apply Strategies for ThinkFolio.
*
* AUTHOR       : Darren. Lin
*
* REFERENCE    : P444
*
* DATE         : 30-Aug-2010
*------------------------------------------------------------------------------
* AMENDMENT HISTORY
*---------------------
* [Truncated to last 5 entries]
*
* NAME    : Darren. Lin
* VERSION : 1.1        DATE: 30-Aug-2010               REF: P444
* PURPOSE : Initial Version.
* 
* NAME    : G. Crawford
* VERSION : 1.2        DATE: 02-Dec-2010               REF: P444
* PURPOSE : Added logging
*----------------------------------------------------------------------------*/
public class ApplyStrategies 
{
	private ThinkTransferDao ttDao;
	private MgLogger log;
	
	public ApplyStrategies(EntityManagerFactory ttemf)
	{
		ttDao=new ThinkTransferDao(ttemf.createEntityManager());
		log = new MgLogger( ApplyStrategies.class );
		assert( log != null );
	
	}
	
	public void executeApplyStrategiesSp()
	{
		log.info("executeApplyStrategiesSp: Execute apply strategies stored proc: start");
		ttDao.executeApplyStrategiesSp();
		log.info("executeApplyStrategiesSp: Execute apply strategies stored proc: end");
	}
}
